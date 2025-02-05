from langchain.callbacks.base import BaseCallbackHandler

class MyCustomCallbackHandler(BaseCallbackHandler):
    """Custom callback handler to track execution steps."""

    def on_llm_start(self, llm, prompts, **kwargs):
        print(f"[CALLBACK] LLM is processing prompts:", prompts)

    def on_llm_end(self, response, **kwargs):
        print("[CALLBACK] LLM generated response:", response.generations)

    def on_tool_start(self, tool, input, **kwargs):
        print(f"[CALLBACK] Tool '{tool}' started with input: {input}")

    def on_tool_end(self, output, **kwargs):
        print(f"[CALLBACK] Tool execution finished. Output: {output}")

    def on_agent_finish(self, finish, **kwargs):
        print(f"[CALLBACK] Final agent output: {finish.return_values}")

