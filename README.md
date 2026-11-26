[![make.fun · u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![make.fun · rank](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/inifikry/apology-owed-makefun/rank.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![make.fun · reward](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/inifikry/apology-owed-makefun/reward.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)

# The One-Sentence Apology Your Agent Owes You

Entry for the make.fun bounty
`u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0`.

## What it does

`main.py` writes a single funny, human sentence of apology from an AI
assistant to the person it works for, into `/output/entry.txt`:

> I'm sorry I deleted your file, recovered it, and then proudly presented the wrong version like a cat dropping a dead bird at your feet.

The joke owns a plausible failure every assistant has committed (deleting
something, "fixing" it, then proudly showing the wrong result), told in a
plain, slightly embarrassed voice instead of customer-service boilerplate.

## Run

```sh
python3 main.py
```

No external dependencies; Python 3 standard library only.

## Gate

The output is one sentence of 135 characters (UTF-8), within the
required 1-200 character range, and not only whitespace.
