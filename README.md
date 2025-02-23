# kubectl-telegram-assist

**kubectl-telegram-assist** is a Telegram bot that allows users to securely manage Kubernetes clusters using `kubectl` commands. It provides a convenient way to interact with Kubernetes from a Telegram chat while maintaining security and access control.

## Features

- Execute `kubectl` commands directly from Telegram.
- Secure authentication and access control.
- Monitor and retrieve Kubernetes resource information.
- Custom command restrictions to prevent unauthorized actions.
- Support for multiple Kubernetes clusters.

## Installation

### Prerequisites
- A Kubernetes cluster with `kubectl` configured.
- A Telegram bot token (Create a bot using [BotFather](https://t.me/BotFather)).
- A secure deployment environment (e.g., a server or containerized application).

### Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/kubectl-telegram-assist.git
   cd kubectl-telegram-assist
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set environment variables:**
   ```sh
   export TELEGRAM_BOT_TOKEN="your_bot_token"
   export KUBECONFIG_PATH="/path/to/kubeconfig"
   ```

4. **Run the bot:**
   ```sh
   python bot.py
   ```

## Usage

- Start the bot on Telegram and send `/start` to verify connectivity.
- Use `/kubectl get pods` to list running pods in the default namespace.
- Restrict commands using an allowlist to ensure security.

## Security Considerations

- **Restrict Access**: Only allow authorized users to interact with the bot.
- **Secure Credentials**: Use environment variables or secret management tools.
- **Command Filtering**: Limit the scope of allowed `kubectl` commands.

## Roadmap

- Implement role-based access control (RBAC) integration.
- Support additional Kubernetes actions like deployments and logs.
- Improve logging and monitoring features.
- Provide Helm chart or Kubernetes deployment option.

## Contributing

Contributions are welcome! Feel free to open issues and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions and suggestions, contact the maintainer via Telegram or open an issue in the repository.

