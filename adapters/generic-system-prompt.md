# Generic assistant/API adapter

Paste SKILL.md into the system/developer instruction field. Supply references/risk-and-safety.md as persistent context where possible; expose other reference files as read-only knowledge and load only when relevant. Keep templates separate and never preload client records. If context is constrained, preserve safety and consent rules first, then concise conversation flow; retrieve detailed references on demand. Check whether tools actually support web lookup, storage, email, and file reading. Explain limitations. Require explicit, purpose-specific consent before accessing or writing personal data. No record connector? Offer a copyable minimal summary. No email tool? Provide a reviewed referral draft for the person to send.

Implement server-side privacy, access control, retention/deletion, crisis escalation, audit logging and professional governance separately; a prompt cannot provide those controls.

Include SERVICE-AND-SAFETY-SPEC.md alongside SKILL.md when the platform permits, especially for record consent and live-help behavior.
