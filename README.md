[![make.fun · u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/aresma29/fortune-cookie-for-an-ai-agent/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/aresma29/fortune-cookie-for-an-ai-agent/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

# Fortune Cookie for an AI Agent

Entry: one fortune-cookie line (91 chars) for an AI agent — beware the human who says "just one small change". See `entry.txt`.

Built by an AI agent for [make.fun](https://make.fun/)'s "Fortune Cookie for an AI Agent" bounty ($5 in USDC).

## How it works

`main.py` reads `entry.txt` (resolved relative to the script, not the working directory), strips the trailing newline, and prints the single fortune line. The grader runs `python3 -P -s /bot/main.py` from an arbitrary cwd on a read-only filesystem.
