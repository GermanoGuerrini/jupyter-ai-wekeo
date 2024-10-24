c = get_config()

c.AiExtension.help_message_template = """
Hi there! I'm the {persona_name}.
You can ask me a question using the text box below. You can also use these commands:
{slash_commands_list}

Jupyter AI includes [magic commands](https://jupyter-ai.readthedocs.io/en/latest/users/index.html#the-ai-and-ai-magic-commands) that you can use in your notebooks.
For more information, see the [documentation](https://jupyter-ai.readthedocs.io).
""".strip()

c.AiExtension.default_language_model = "wekeo-provider:server"
c.AiExtension.allowed_providers = ["wekeo-provider"]
c.AiExtension.default_max_chat_history = None
