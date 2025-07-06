# How Our Git Workflow Works — The Temporary Branch (“Meta”) Strategy Explained

Hey team! I want to share a quick explanation of how our Git branches work and why we use a temporary branch called `dev` for integration and testing before pushing to production.

---

## The Problem with Git and Staying Up to Date

When you try to create a pull request (PR) into a branch (like `main`, `frontend`, or `backend`), Git checks if your branch is up to date with the target branch.

- If the target branch has new commits you don’t have, Git will ask you to update your branch (pull) before merging.
- This can cause merge conflicts and slow us down, especially if branches have been diverging for a while.

---

## Our Solution: The Temporary `dev` Branch

To avoid these conflicts and keep things simple:

1. Every time we have a new batch of changes ready for testing, I create a **brand new `dev` branch** fresh from the current `main` branch.

2. Then, I merge the latest shared `frontend` and `backend` branches into this new `dev` branch.

3. We run all our unit tests and checks on this clean, temporary `dev` branch.

4. Once everything passes, we merge `dev` into `main` for production.

5. After that, we **delete the `dev` branch** — it disappears.

6. Next time, we repeat: create a fresh `dev` from `main` and merge `frontend`/`backend` again.

---

## Why This Works

- Because `dev` is brand new every time and starts exactly where `main` is, Git won’t ask you to stay up to date with `main` when you PR into `dev`.
- This saves us from lots of unnecessary merge conflicts and update headaches.
- Also, we never PR directly into `main` — only into `dev`, so `main` stays clean and stable.

---

## What This Means for You

- You will have your own personal `frontend` and `backend` branches for your work.
- Your personal branches will need to be **regularly updated by pulling** from the shared `frontend` and `backend` branches to avoid conflicts when making PRs.
- But when you PR into the temporary `dev` branch (via `frontend`/`backend`), you won’t have to worry about staying up to date with `main` because `dev` is always fresh.
- This keeps your PRs simpler and integration smoother.

---

## Summary

| You Work On                        | PRs To                     | You Need To Keep Up To Date With         | Git Will Ask You To Stay Up To Date With          |
|----------------------------------|----------------------------|------------------------------------------|---------------------------------------------------|
| Personal branches (`frontend`/`backend`) | Shared `frontend`/`backend` branches | Shared `frontend`/`backend` branches         | Yes, regularly — to avoid conflicts                |
| Shared `frontend`/`backend` branches       | Temporary `dev` branch              | — (freshly created from `main`)               | No, because `dev` is always fresh from `main`      |
| Temporary `dev` branch                     | `main` branch                      | `main` branch                                  | Possibly, if `main` changes during testing         |

---

Feel free to ask me anytime if you want help updating your personal branches or if you’re confused about the flow!

---

# How to Keep Your Branch Updated (Using `git pull`)

### Why keep your branch updated?

Your personal `frontend` or `backend` branch is based on the shared `frontend`/`backend` branches. As others merge their changes, the shared branches move ahead. To avoid conflicts when you create a pull request (PR), you need to regularly update your branch with those latest changes.

---

### How to update your branch: Use `git pull`

Before pushing your changes or creating a PR:

- For `frontend` branch:
  ```bash
  git pull origin frontend
