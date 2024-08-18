//! You can run this script using the following command:
//! ```shell
//! RUST_LOG=info cargo run --release
//! ```

use alloy_sol_types::SolType;
use anime_taste_proof_lib::PublicValuesStruct;
use clap::Parser;
use sp1_sdk::{ProverClient, SP1ProofWithPublicValues, SP1Stdin};
use std::fs::File;
use std::io::Write;

pub const ANIME_TASTE_PROOF_ELF: &[u8] = include_bytes!("../../../elf/riscv32im-succinct-zkvm-elf");

#[derive(Parser, Debug)]
#[clap(author, version, about, long_about = None)]
struct Args {
    #[clap(long)]
    execute: bool,

    #[clap(long)]
    prove: bool,
}

fn main() {
    sp1_sdk::utils::setup_logger();

    let client = ProverClient::new();
    let stdin = SP1Stdin::new();

    let (public_values, report) = client
        .execute(ANIME_TASTE_PROOF_ELF, stdin.clone())
        .run()
        .unwrap();

    println!("Public values: {}", public_values.raw());
    println!("Number of cycles: {}", report.total_instruction_count());
    println!("Program executed successfully.");

    let decoded: PublicValuesStruct =
        PublicValuesStruct::abi_decode(public_values.as_slice(), true).unwrap();

    let PublicValuesStruct {
        username,
        time_stamp,
        score_list,
    } = decoded;

    println!("username: {}", username);
    println!("time_stamp: {}", time_stamp);
    println!("score: {:?}", score_list);

    let json_data = serde_json::to_string_pretty(&PublicValuesStruct {
        username: username.clone(),
        time_stamp: time_stamp.clone(),
        score_list: score_list.clone(),
    })
    .expect("Failed to serialize struct to JSON");

    let mut file = File::create("decoded-output.json").expect("Failed to create file");
    file.write_all(json_data.as_bytes())
        .expect("Failed to write JSON to file");

    println!("Saved PublicValuesStruct to decoded-output.json");

    let (pk, vk) = client.setup(ANIME_TASTE_PROOF_ELF);
    let proof = client.prove(&pk, stdin).plonk().run().unwrap();
    let solidity_proof = proof.raw();

    println!("proof: {:?}", solidity_proof);
    println!("generated proof");

    client.verify(&proof, &vk).expect("verification failed");
    proof.save("proof.bin").expect("saving proof failed");

    let deserialized_proof =
        SP1ProofWithPublicValues::load("proof.bin").expect("loading proof failed");

    client
        .verify(&deserialized_proof, &vk)
        .expect("verification failed");

    println!("successfully generated and verified proof for the program!")
}
