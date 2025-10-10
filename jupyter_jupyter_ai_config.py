c = get_config()

c.AiExtension.default_language_model = "wekeo-provider:server"
c.AiExtension.allowed_providers = ["wekeo-provider", "openai", "openai-chat"]
c.AiExtension.default_max_chat_history = None

c.AiExtension.model_parameters = {
    "wekeo-provider:server": {"endpoint": "<http://wekeo-llm-server-endpoint>/rag"}
}
