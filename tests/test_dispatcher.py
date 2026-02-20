from squad_manager.core.dispatcher import build_command


def test_build_command_includes_yolo_flag() -> None:
    """Test that the generated command includes the --yolo flag."""
    command = build_command("grunt", "Fix the bug")
    assert "--yolo" in command, "Command must include --yolo flag"


def test_build_command_includes_r_flag() -> None:
    """Test that the generated command includes the -r flag."""
    command = build_command("grunt", "Fix the bug")
    assert "-r" in command, "Command must include -r flag"


def test_build_command_includes_model_flag() -> None:
    """Test that the generated command includes the explicit model declaration."""
    command = build_command("grunt", "Fix the bug")
    assert "--model" in command, "Command must specify the model using --model flag"

    model_index = command.index("--model")
    assert model_index + 1 < len(command), "--model flag missing value"
    assert command[model_index + 1] == "gemini-3.1-pro-preview", (
        "Model must be gemini-3.1-pro-preview"
    )
