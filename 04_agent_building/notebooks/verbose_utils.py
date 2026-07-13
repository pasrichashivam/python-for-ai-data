import json
from typing import Any


SEPARATOR = "<---------------------------------->"
DOUBLE_LINE = "=" * 70

def pretty_json(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False)


def print_title(title: str) -> None:
    print("\n" + DOUBLE_LINE)
    print(title)
    print(DOUBLE_LINE)


def print_separator() -> None:
    print(SEPARATOR)


def print_memory(messages: list[dict], heading: str = "Conversation memory") -> None:
    print_title(heading)
    print(f"Memory contains {len(messages)} message(s)\n")

    for index, msg in enumerate(messages):
        print(f"[{index}] ROLE: {msg.get('role')}")
        if "content" in msg and msg["content"] is not None:
            print("CONTENT:")
            print(msg["content"])
        else:
            print("CONTENT: None")

        if msg.get("tool_calls"):
            print("TOOL CALLS:")
            for i, call in enumerate(msg["tool_calls"], start=1):
                fn = call["function"]["name"]
                args = call["function"]["arguments"]
                print(f"  {i}. id: {call['id']}")
                print(f"     name: {fn}")
                print(f"     arguments: {args}")

        if msg.get("tool_call_id"):
            print(f"TOOL CALL ID: {msg['tool_call_id']}")

        print("-" * 70)


def print_tool_schemas(tool_schemas: list[dict]) -> None:
    print_title("Available tool schemas")
    for i, schema in enumerate(tool_schemas, start=1):
        fn = schema["function"]
        print(f"{i}. NAME: {fn['name']}")
        print(f"   DESCRIPTION: {fn['description']}")
        print("   ARGUMENTS:")
        print(pretty_json(fn["parameters"]))
        print("-" * 60)


def print_raw_llm_message(message: Any) -> None:
    print_title("Raw LLM response")
    print("assistant.content:")
    print(message.content)
    print("\nassistant.tool_calls:")
    if not message.tool_calls:
        print("None")
        return

    for i, call in enumerate(message.tool_calls, start=1):
        print(f"\nTool call #{i}")
        print(f"  id: {call.id}")
        print(f"  name: {call.function.name}")
        print(f"  arguments (raw): {call.function.arguments}")


def print_tool_execution(tool_name: str, arguments: dict, result: Any) -> None:
    print_title("Tool execution")
    print(f"Requested tool: {tool_name}")
    print("Parsed arguments:")
    print(pretty_json(arguments))
    print("\nResult returned by Python:")
    print(result)
