from django.shortcuts import redirect
from django.urls import reverse, resolve
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.conf import settings

class OTPRequiredMiddleware:
    """
    强制管理员用户设置2FA的中间件
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # 预先解析安全URL，提高性能并避免每次请求都计算
        self.setup_url = reverse('two_factor:setup')
        self.login_url = reverse('two_factor:login')
        self.qr_code_url = reverse('two_factor:qr')
        self.logout_url = reverse('admin:logout')
        # 安全路径列表 - 这些路径不需要2FA
        self.safe_paths = [
            self.setup_url,
            self.login_url,
            self.qr_code_url,
            self.logout_url,
            # 可以添加其他不需要2FA的路径
        ]

    def __call__(self, request):
        # 在视图处理前进行检查
        if request.user.is_authenticated and not self._is_safe_path(request.path):
            # 检查用户是否为 staff 且未设置 2FA
            if request.user.is_staff and not TOTPDevice.objects.filter(user=request.user, confirmed=True).exists():
                # 如果是，则重定向到 2FA 设置页面
                return redirect(self.setup_url)

        # 如果检查通过，则继续处理请求并获取响应
        response = self.get_response(request)


        return response
        
    def _is_safe_path(self, path):
        """
        检查给定的路径是否为安全路径，无需进行2FA检查。
        """
        # 对于设置URL，我们需要检查前缀，因为它是一个多步骤的向导
        if path.startswith(self.setup_url):
            return True

        # 对于其他URL，我们可以使用精确匹配
        return path in self.safe_paths
