# Configuration

Machine-specific and environment-specific values used by skills during document generation. Update these values when setting up on a new machine or after modifying your Python environment.

---

## Python Environment

**Python executable path (python-docx operations):**
`C:/Users/delos/miniconda3/envs/agents/python.exe`

This path is used by any skill that generates or reads `.docx` files: `cv_targeted`, `cv_general`, `interview_prep`, `followup`. Update this value if your conda environment changes or you are setting up on a new machine.

Skills load this file at the phase where Python execution is required. Do not hardcode the path in skill files — always reference this file as the single source of truth.
