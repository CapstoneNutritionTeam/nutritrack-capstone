# Use a lightweight Python image
FROM python:3.11-slim

# Install git, curl, sudo (for GitHub CLI)
RUN apt-get update && apt-get install -y git curl sudo gnupg2

# Install GitHub CLI (optional but recommended)
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | \
    gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | \
    tee /etc/apt/sources.list.d/github-cli.list > /dev/null && \
    apt-get update && apt-get install -y gh

# Create a non-root user to avoid running as root inside the container
RUN useradd -ms /bin/bash devuser && adduser devuser sudo

# Set working directory
WORKDIR /home/devuser/app

# Copy requirements.txt before switching user and install dependencies system-wide
COPY requirements.txt .

# Install dependencies as root (no --user)
RUN pip install -r requirements.txt

# Now copy rest of your code and change ownership to devuser
COPY --chown=devuser:devuser . .

# Switch to non-root user
USER devuser

# Default command when container runs
CMD ["bash"]
