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


def print_info_before_llm_call(turn_number, messages, TOOL_SCHEMAS, model):
    print_separator()
    print_title(f"AGENT LOOP TURN {turn_number}")
    print_memory(messages, "Memory BEFORE API call")
    print_tool_schemas(TOOL_SCHEMAS)
    print_title("Sending everything to the model")
    print(f"Model: {model}")
    print("What the model receives:")
    print("- conversation memory")
    print("- tool schemas")
    print("- max_tokens setting")
    print("- the current instruction context")
    print("\nImportant: the model does NOT run Python code.")
    print("It only decides whether it needs a tool or can answer directly.")
    print_separator()

def print_memory_state_after_assistant_message(messages):
    print_title("No tool calls detected")
    print("The model answered directly, so the loop stops here.")
    print_memory(messages, "Memory AFTER final assistant answer")
    print_separator()

def print_memory_state_after_tool_request(messages):
    print_title("Assistant requested tool call(s)")
    print("The assistant message has been added to memory.")
    print("Now Python will inspect each requested tool call and execute it.")
    print_memory(messages, "Memory AFTER assistant tool request")

def print_tool_call_process(call, TOOLS_BY_NAME):
    print_title("Processing one tool call")
    print(f"Tool call id: {call.id}")
    print(f"Tool name   : {call.function.name}")
    print(f"Raw args    : {call.function.arguments}")
    print("Parsed args  :")
    print(pretty_json(json.loads(call.function.arguments)))
    print("\nLooking up the tool in TOOLS_BY_NAME...")
    print(f"Available tools: {list(TOOLS_BY_NAME.keys())}")

def print_memory_state_after_tool_call(messages):
    print_title("Tool result added to memory")
    print("The tool output has now been stored as a TOOL message.")
    print_memory(messages, "Memory AFTER tool result")
    print("Why do we loop again?")
    print("Because the model has the tool result only after this step.")
    print("Now it can read the result and produce the final natural-language answer.")
    print_separator()