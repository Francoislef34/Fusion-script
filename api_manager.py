import random

class ApiManager:
    def __init__(self):
        self.api_keys = {
            "DEEPSEEK_KEYS": ["sk-ef08317d125947b3a1ce5916592bef00", "sk-d73750d96142421cb1098c7056dd7f01"],
            "SERPER_KEYS": ["047b30db1df999aaa9c293f2048037d40c651439"],
            "GEMINI_API_KEYS": ["AIzaSyBWXcwGdzoeUzbApSNLICkanNcm7BYzYcs", "AIzaSyAk6Ph25xuIY3b5o-JgdL652MvK4usp8Ms", "AIzaSyDuccmfiPSk4042NeJCYIjA8EOXPo1YKXU", "AIzaSyAQq6o9voefaDxkAEORf7W-IB3QbotIkwY", "AIzaSyDYaYrQQ7cwYFm8TBpyGM3dJweOGOYl7qw"],
            "GUARDIAN_KEY": ["07c622c1-af05-4c24-9f37-37d219be76a0"],
        }

        # Structure based on user's successful test results
        self.working_endpoints = [
            # DeepSeek Key Successes
            {'service': 'DeepSeek Models', 'key_name': 'DEEPSEEK_KEYS', 'url': 'https://api.deepseek.com/models', 'method': 'GET', 'auth_header': 'Authorization', 'auth_prefix': 'Bearer '},
            {'service': 'Shodan Host Info', 'key_name': 'DEEPSEEK_KEYS', 'url': 'https://api.shodan.io/shodan/host/8.8.8.8', 'method': 'GET', 'param_name': 'key'},
            {'service': 'Pulsedive Analyze', 'key_name': 'DEEPSEEK_KEYS', 'url': 'https://pulsedive.com/api/v1/analyze.php', 'method': 'GET', 'param_name': 'key'},
            {'service': 'LoginRadius Ping', 'key_name': 'DEEPSEEK_KEYS', 'url': 'https://api.loginradius.com/identity/v2/auth/ping', 'method': 'GET', 'auth_header': 'X-LoginRadius-Api-Key'},

            # Serper Key Successes
            {'service': 'Serper Search', 'key_name': 'SERPER_KEYS', 'url': 'https://google.serper.dev/search', 'method': 'POST', 'auth_header': 'X-API-KEY'},
            {'service': 'Serper Images', 'key_name': 'SERPER_KEYS', 'url': 'https://google.serper.dev/images', 'method': 'POST', 'auth_header': 'X-API-KEY'},
            {'service': 'Shodan Host Info', 'key_name': 'SERPER_KEYS', 'url': 'https://api.shodan.io/shodan/host/8.8.8.8', 'method': 'GET', 'param_name': 'key'},
            {'service': 'Pulsedive Analyze', 'key_name': 'SERPER_KEYS', 'url': 'https://pulsedive.com/api/v1/analyze.php', 'method': 'GET', 'param_name': 'key'},
            {'service': 'LoginRadius Ping', 'key_name': 'SERPER_KEYS', 'url': 'https://api.loginradius.com/identity/v2/auth/ping', 'method': 'GET', 'auth_header': 'X-LoginRadius-Api-Key'},

            # Gemini Key Successes
            {'service': 'Gemini Generate Content', 'key_name': 'GEMINI_API_KEYS', 'url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent', 'method': 'POST', 'param_name': 'key'},
            {'service': 'Gemini Models List', 'key_name': 'GEMINI_API_KEYS', 'url': 'https://generativelanguage.googleapis.com/v1beta/models', 'method': 'GET', 'param_name': 'key'},
            {'service': 'Shodan Host Info', 'key_name': 'GEMINI_API_KEYS', 'url': 'https://api.shodan.io/shodan/host/8.8.8.8', 'method': 'GET', 'param_name': 'key'},
            {'service': 'Pulsedive Analyze', 'key_name': 'GEMINI_API_KEYS', 'url': 'https://pulsedive.com/api/v1/analyze.php', 'method': 'GET', 'param_name': 'key'},
            {'service': 'LoginRadius Ping', 'key_name': 'GEMINI_API_KEYS', 'url': 'https://api.loginradius.com/identity/v2/auth/ping', 'method': 'GET', 'auth_header': 'X-LoginRadius-Api-Key'},

            # Guardian Key Successes
            {'service': 'Guardian Content', 'key_name': 'GUARDIAN_KEY', 'url': 'https://content.guardianapis.com/search', 'method': 'GET', 'param_name': 'api-key'},
            {'service': 'Shodan Host Info', 'key_name': 'GUARDIAN_KEY', 'url': 'https://api.shodan.io/shodan/host/8.8.8.8', 'method': 'GET', 'param_name': 'key'},
            {'service': 'Pulsedive Analyze', 'key_name': 'GUARDIAN_KEY', 'url': 'https://pulsedive.com/api/v1/analyze.php', 'method': 'GET', 'param_name': 'key'},
            {'service': 'LoginRadius Ping', 'key_name': 'GUARDIAN_KEY', 'url': 'https://api.loginradius.com/identity/v2/auth/ping', 'method': 'GET', 'auth_header': 'X-LoginRadius-Api-Key'},
        ]
        # Note: The user mentioned 25 endpoints, but the provided success list contains 18 unique combinations.
        # I will implement based on the provided list. The other mentioned endpoints (like WolframAlpha, Twilio, etc.)
        # were in a larger list but did not have a corresponding "✅ Succès" entry with a key type.

    def get_api_details(self, service: str):
        """
        Trouve une configuration fonctionnelle pour un service donné.
        Retourne un dictionnaire avec l'URL, la méthode, la clé, et comment l'utiliser.
        """
        possible_endpoints = [e for e in self.working_endpoints if e['service'] == service]
        if not possible_endpoints:
            raise ValueError(f"Aucune configuration API fonctionnelle trouvée pour le service : {service}")

        # Choisir un endpoint au hasard s'il y en a plusieurs
        endpoint = random.choice(possible_endpoints)

        key_name = endpoint['key_name']
        key_value = random.choice(self.api_keys[key_name])

        details = {
            'url': endpoint['url'],
            'method': endpoint['method'],
            'key': key_value
        }

        if 'auth_header' in endpoint:
            auth_prefix = endpoint.get('auth_prefix', '')
            details['headers'] = {endpoint['auth_header']: f"{auth_prefix}{key_value}"}
        elif 'param_name' in endpoint:
            details['params'] = {endpoint['param_name']: key_value}

        return details

# Example usage:
if __name__ == '__main__':
    manager = ApiManager()

    try:
        # Get details for a service
        serper_details = manager.get_api_details('Serper Search')
        print(f"Serper Search details: {serper_details}")

        gemini_details = manager.get_api_details('Gemini Generate Content')
        print(f"Gemini details: {gemini_details}")

        # Example of a cross-matched service
        shodan_details = manager.get_api_details('Shodan Host Info')
        print(f"Shodan details (using a random valid key): {shodan_details}")

    except ValueError as e:
        print(e)
