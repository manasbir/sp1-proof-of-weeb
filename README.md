# Anime Taste Validator - ZK Proof Hackathon Project

## Overview

Welcome to the Anime Taste Validator! This project allows users to prove the validity of their anime taste using zero-knowledge proofs (ZKPs). By integrating with MyAnimeList (MAL) and using the Succinct SP1 ZKVM circuit, users can generate cryptographic proofs that demonstrate their anime preferences without revealing unnecessary details.

## Features

- **OAuth Integration**: Easily log in with your MyAnimeList account to fetch your anime list and profile information.
- **Zero-Knowledge Proof Generation**: After logging in, generate a ZK proof using the Succinct SP1 ZKVM circuit that outputs:
  - Public badges
  - Proof bytes
  - Timestamps
  - Username
- **Badge System**: Based on your anime list, earn different badges such as:
  - **Based**: High-quality and well-curated taste
  - **Age**: Anime selections influenced by your age
  - **Degen**: Obsession with certain genres or niche selections
  - **Normie**: Mainstream and popular anime choices
  - **Completionist**: High completion rate across anime series
  - **Ranked**: Active engagement in ranking and rating shows

## How It Works

1. **Log In with MyAnimeList**: Authenticate via OAuth to connect your MAL account.
2. **Generate Proof**: Once authenticated, generate a ZK proof using our circuit that validates your taste based on your list. The circuit outputs proof data and public return values.
3. **Badge Assignment**: Based on your proof, you'll be awarded badges that reflect your anime taste. These badges are displayed on your profile page.
4. **Prove Your Taste**: Share your profile to prove your anime preferences with zero knowledge—no need to expose your full list or personal information.

## Technical Details

- **Frontend**: Built with React and integrated with MyAnimeList OAuth for authentication and data fetching.
- **ZK Circuit**: We leverage the Succinct SP1 ZKVM circuit to generate proofs. The circuit processes anime list data and outputs proof bytes along with public return values.
- **Backend**: Node.js handles the proof generation and verification process, alongside badge assignment based on proof results.

## Getting Started

### Prerequisites

- Node.js (v16 or later)
- Yarn or npm
- MyAnimeList Account

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo/anime-taste-validator.git
    cd anime-taste-validator
    ```

2. Install dependencies:

    ```bash
    yarn install
    ```

3. Set up environment variables:
    - `MAL_CLIENT_ID` - Your MyAnimeList OAuth client ID
    - `MAL_CLIENT_SECRET` - Your MyAnimeList OAuth client secret

4. Run the application:

    ```bash
    yarn start
    ```

5. Open the app in your browser at `http://localhost:3000`.

## Usage

1. Log in using your MyAnimeList account.
2. View your fetched anime list on the dashboard.
3. Click on "Generate Proof" to create a ZK proof based on your list.
4. Earn badges and share your profile to showcase your anime taste!

## Contributing

We welcome contributions! Please submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Succinct Labs](https://succinct.xyz/) for providing the SP1 ZKVM circuit.
- The MyAnimeList API for authentication and data access.
