"""dp_config.py — Shared constants for Daily Planning scripts."""

PKM_BASE = "/opt/myPKA"
TODOIST_API = "https://api.todoist.com/api/v1"
RESOURCE_PREFIXES = ('*', '📂', '🎯', '📅', '♻️')

# Projects that define PPM scope (Inbox + 👤-tree)
PPM_PARENTS = {
    '6XmgqfxmFFQjGG6w',  # Inbox
    '6cFcm2MpmHvc2F3H',  # 👤 PERSONAL
    '6c8XR7HXhgMWMWwj',  # 👤 PROJECTS
}

# Projects that define BPM scope (💼-trees)
BPM_PARENTS = {
    '6fC99W283Jw2cjV2',  # 💼 KAMER E-COMMERCE
    '6gfFMpGVh5WJHPCx',  # PROJECTS (under KE)
    '6gfFMpHcMCQvPQpc',  # 💼 GELDSTROOM REGIE
    '6gfFMpmXQ3RCGgMC',  # 💼 PROJECTS (under GR)
}

PPM_GOALS_DIR    = f"{PKM_BASE}/PKM/My Life/Goals"
PPM_PROJECTS_DIR = f"{PKM_BASE}/PKM/My Life/Projects"

BPM_GOALS_DIRS    = [
    f"{PKM_BASE}/Team Knowledge/Kamer E-commerce/Goals",
    f"{PKM_BASE}/Team Knowledge/Geldstroom Regie/Goals",
]
BPM_PROJECTS_DIRS = [
    f"{PKM_BASE}/Team Knowledge/Kamer E-commerce/Projects",
    f"{PKM_BASE}/Team Knowledge/Geldstroom Regie/Projects",
]


def get_goals_dirs(domain: str) -> list:
    if domain == 'ppm':
        return [PPM_GOALS_DIR]
    return [d for d in BPM_GOALS_DIRS if __import__('os').path.isdir(d)]


def get_projects_dirs(domain: str) -> list:
    if domain == 'ppm':
        return [PPM_PROJECTS_DIR]
    return [d for d in BPM_PROJECTS_DIRS if __import__('os').path.isdir(d)]

NL_MONTHS = {
    1: 'jan', 2: 'feb', 3: 'mrt', 4: 'apr', 5: 'mei', 6: 'jun',
    7: 'jul', 8: 'aug', 9: 'sep', 10: 'okt', 11: 'nov', 12: 'dec',
}


def get_domain_ids(projects: list, domain: str) -> dict:
    """Return {project_id: name} for all projects in the given domain."""
    parents = PPM_PARENTS if domain == 'ppm' else BPM_PARENTS
    return {
        p['id']: p.get('name', p['id'])
        for p in projects
        if p['id'] in parents or (p.get('parent_id') or '') in parents
    }


def filter_tasks(tasks: list, domain_ids: set) -> list:
    """Keep only tasks in scope, drop resource tasks."""
    return [
        t for t in tasks
        if t.get('project_id') in domain_ids
        and not any(t.get('content', '').startswith(p) for p in RESOURCE_PREFIXES)
    ]


def fmt_deadline(deadline_str: str, today) -> str:
    """Format deadline with days-remaining and urgency indicator."""
    from datetime import date
    if not deadline_str or not deadline_str.strip():
        return '—'
    try:
        d = date.fromisoformat(deadline_str.strip())
    except ValueError:
        return '—'
    days = (d - today).days
    month = NL_MONTHS[d.month]
    label = f"{d.day} {month}"
    if days <= 14:
        return f"{label} ({days}d) 🔥"
    if days <= 45:
        return f"{label} ({days}d) ⚠️"
    return label
