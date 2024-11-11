c = get_config()  # noqa: F821

c.AiExtension.default_language_model = "wekeo-provider:server"
c.AiExtension.allowed_providers = ["wekeo-provider", "openai", "openai-chat"]
c.AiExtension.default_max_chat_history = None
