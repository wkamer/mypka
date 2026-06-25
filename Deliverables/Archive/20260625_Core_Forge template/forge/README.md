# Forge

A scaffolding folder that stamps out a new web service / app project with a
high-performing AI agent team and a state-of-the-art delivery process already
wired in.

## Create a project

```bash
make new
# or:
bash bin/new-project.sh
```

You'll be prompted for: project name, slug, one-line vision, owner, stack,
whether it has a UI, whether it has AI components, and where to put it.
Forge then copies `template/`, stamps your answers in, seeds env files, and
(optionally) runs `git init` + a first commit.

Start working:

```bash
cd <destination>/<slug>
claude .     # Larry boots from CLAUDE.md, Gate 1 (Discovery) is open
```

## Layout

```
forge/
├── bin/new-project.sh   the bootstrapper (prompts + stamps)
├── Makefile             `make new`
└── template/            the golden project skeleton that gets copied
```

Edit `template/` to evolve what every future project starts with.
Never edit a generated project to change the template — change `template/`.
