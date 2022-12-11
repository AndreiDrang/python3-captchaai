Serializer
==========

To import this module:

.. code-block:: python

    from python3_captchaai.core import serializer


.. autopydantic_model:: core.serializer.PostRequestSer
    :members:
    :undoc-members:

.. autopydantic_model:: core.serializer.TaskSer
    :members:
    :undoc-members:

.. autopydantic_model:: core.serializer.RequestCreateTaskSer
    :members:
    :undoc-members:

.. autopydantic_model:: core.serializer.RequestGetTaskResultSer
    :members:
    :undoc-members:

.. autopydantic_model:: core.serializer.ResponseSer
    :members:
    :undoc-members:

.. autopydantic_model:: core.serializer.CaptchaResponseSer
    :inherited-members: ResponseSer
    :members:
    :undoc-members:

.. autopydantic_model:: core.serializer.ControlResponseSer
    :inherited-members: ResponseSer
    :members:
    :undoc-members:

.. autopydantic_model:: core.serializer.CaptchaOptionsSer
    :members:
    :undoc-members:

.. autopydantic_model:: core.serializer.WebsiteDataOptionsSer
    :members:
    :undoc-members:

.. autopydantic_model:: core.serializer.ProxyDataOptionsSer
    :inherited-members: WebsiteDataOptionsSer
    :members:
    :undoc-members:

.. autopydantic_model:: core.serializer.ReCaptchaV3ProxyLessOptionsSer
    :inherited-members: WebsiteDataOptionsSer
    :members:
    :undoc-members:

.. autopydantic_model:: core.serializer.ReCaptchaV3OptionsSer
    :inherited-members: ReCaptchaV3ProxyLessOptionsSer, ProxyDataOptionsSer
    :members:
    :undoc-members:

.. autopydantic_model:: core.serializer.HCaptchaOptionsSer
    :members:
    :undoc-members:
