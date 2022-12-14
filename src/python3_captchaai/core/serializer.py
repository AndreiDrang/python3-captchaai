from typing import Any, Dict, List, Optional

from pydantic import Field, BaseModel, conint, constr

from python3_captchaai.core.enum import ProxyType, CaptchaTypeEnm, ResponseStatusEnm
from python3_captchaai.core.config import APP_ID

"""
HTTP API Request ser
"""


class PostRequestSer(BaseModel):
    clientKey: str = Field(..., description="Client account key, can be found in user account")


class TaskSer(BaseModel):
    type: CaptchaTypeEnm = Field(..., description="Task type name")


class RequestCreateTaskSer(PostRequestSer):
    task: Optional[TaskSer] = Field(None, description="Task object")
    appId: str = Field(APP_ID, description="AppID", const=True)


class RequestGetTaskResultSer(PostRequestSer):
    taskId: Optional[str] = Field(None, description="ID created by the createTask method")


"""
HTTP API Response ser
"""


class ResponseSer(BaseModel):
    errorId: bool = Field(False, description="Error message: `False` - no error, `True` - with error")
    # error info
    errorCode: Optional[str] = Field(None, description="Error code")
    errorDescription: Optional[str] = Field(None, description="Error description")


class CaptchaResponseSer(ResponseSer):
    taskId: Optional[str] = Field(None, description="Task ID for future use in getTaskResult method.")
    # TODO check docs, this field some times is `status` and some times its `state`
    status: ResponseStatusEnm = Field(ResponseStatusEnm.Processing, description="Task current status", alias="state")
    solution: Dict[str, Any] = Field(None, description="Task result data. Different for each type of task.")

    class Config:
        allow_population_by_field_name = True


class ControlResponseSer(ResponseSer):
    balance: Optional[float] = Field(0, description="Account balance value in USD")
    packages: List = Field(None, description="Monthly Packages")


"""
Other ser
"""


class CaptchaOptionsSer(BaseModel):
    api_key: constr(min_length=36, max_length=36)
    sleep_time: conint(ge=5)


"""
Captcha tasks ser
"""


class WebsiteDataOptionsSer(BaseModel):
    websiteURL: str = Field(..., description="Address of a webpage with Captcha")
    websiteKey: str = Field(..., description="Website key")


class ProxyDataOptionsSer(BaseModel):
    proxyType: ProxyType = Field(..., description="Type of the proxy")
    proxyAddress: str = Field(
        ...,
        description="Proxy IP address IPv4/IPv6."
        "Not allowed to use:"
        "host names instead of IPs,"
        "transparent proxies (where client IP is visible),"
        "proxies from local networks (192.., 10.., 127...)",
    )
    proxyPort: int = Field(..., description="Proxy port.")


class ReCaptchaV3ProxyLessOptionsSer(WebsiteDataOptionsSer):
    pageAction: str = Field(
        "verify",
        description="Widget action value."
        "Website owner defines what user is doing on the page through this parameter",
    )


class ReCaptchaV3OptionsSer(ReCaptchaV3ProxyLessOptionsSer, ProxyDataOptionsSer):
    pass


class HCaptchaOptionsSer(WebsiteDataOptionsSer, ProxyDataOptionsSer):
    pass


class HCaptchaClassificationOptionsSer(BaseModel):
    queries: List[str] = Field(..., description="Base64-encoded images, do not include 'data:image/***;base64,'")
    question: str = Field(
        ..., description="Question ID. Support English and Chinese, other languages please convert yourself"
    )


class GeeTestProxyLessOptionsSer(BaseModel):
    websiteURL: str = Field(..., description="Address of a webpage with Geetest")
    gt: str = Field(..., description="The domain public key, rarely updated")


class GeeTestOptionsSer(GeeTestProxyLessOptionsSer, ProxyDataOptionsSer):
    pass


class FunCaptchaProxyLessOptionsSer(BaseModel):
    websiteURL: str = Field(..., description="Address of a webpage with Funcaptcha")
    websitePublicKey: str = Field(..., description="Funcaptcha website key.")
    funcaptchaApiJSSubdomain: str = Field(
        ...,
        description="A special subdomain of funcaptcha.com, from which the JS captcha widget should be loaded."
        "Most FunCaptcha installations work from shared domains.",
    )


class FunCaptchaOptionsSer(FunCaptchaProxyLessOptionsSer, ProxyDataOptionsSer):
    pass


class DatadomeSliderOptionsSer(ProxyDataOptionsSer):
    websiteURL: str = Field(..., description="Address of a webpage with DatadomeSlider")
    captchaUrl: str = Field(..., description="Captcha Url where is the captcha")


class MtCaptchaOptionsSer(WebsiteDataOptionsSer):
    proxy: str = Field(..., description="String with proxy connection params, example: `198.22.3.1:10001:user:pwd`")


class KasadaOptionsSer(ProxyDataOptionsSer):
    pageURL: str = Field(..., description="Address of a webpage with Kasada")
    proxyLogin: str = Field(
        ...,
        description="Login for proxy which requires authorizaiton (basic)."
        "This isn???t required if you are using proxies authenticated by IP",
    )
    proxyPassword: str = Field(..., description="This isn???t required if you are using proxies authenticated by IP")
