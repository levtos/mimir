"""Explicit authoring-v2 commands for isolated development and acceptance fixtures."""

from typing import Any
from uuid import uuid4


async def activate_draft(runtime: Any, draft: dict[str, Any], **overrides: Any) -> Any:
    preview = await runtime.submit("draft_preview", {"draft_id": draft["draft_id"]})
    return await runtime.submit(
        "activate",
        {
            "draft_id": draft["draft_id"],
            "draft_version": draft["draft_version"],
            "request_id": str(uuid4()),
            "comparison_digest": preview["comparison_digest"],
            "confirmations": preview["required_confirmations"],
            "expected_active_revision": runtime.state.active_revision,
            **overrides,
        },
    )
