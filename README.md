Summarized process: (features -> bugfixes -> dev -> FINAL STAGE: main -> upload using Render.com) 
# Git Branch Workflow and Collaboration Process

This project follows a structured branching model to ensure high-quality code and smooth collaboration among team members.

## Branches and Their Purpose

| Branch         | Purpose                                                     |
|----------------|-------------------------------------------------------------|
| `main`         | Production-ready code. Stable and fully tested.             |
| `dev`          | Integration branch where all tested and approved changes are merged before production. |
| `documentation`| For updating project documentation. Changes here must be reviewed first. |
| `features`     | Branch for developing new features. Feature branches are created from here. |
| `bugfixes`     | Branch for fixing bugs found in features or during integration. |

---

## Workflow Hierarchy

1. **Documentation**:  
  GitHub has a feature called 'Wiki,' which you’ll see as one of the options whenever you design something and want to provide documentation for grading or to keep track of changes—just add it there.

3. **Features**:  
   After documentation is reviewed and approved, new feature branches are created from the `features` branch. Features are developed and tested here. (Add the raw new code here!)

4. **Bugfixes**:  
   Once a feature is ready, it is merged into the `bugfixes` branch for thorough bug fixing and validation.

5. **Dev**:  
   After passing all bug fixes and quality checks, changes from `bugfixes` are merged into `dev` for final integration and team testing.

6. **Main**:  
   When `dev` is stable and tested, it is merged into `main` for production deployment.

---

## Pull Request and Approval Process

- All merges to any branch require a Pull Request (PR).
- Each PR requires **at least 3 team member approvals** before merging.
- This process enforces code review and collaboration standards.
- Branch protection rules are enabled to enforce these PR requirements.


