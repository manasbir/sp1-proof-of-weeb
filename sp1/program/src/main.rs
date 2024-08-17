#![no_main]
sp1_zkvm::entrypoint!(main);

use alloy_sol_types::SolType;
use anime_taste_proof_lib::{PublicValuesStruct, ScoreListStruct};
use serde::{Deserialize, Serialize};
use std::fs;

#[derive(Serialize, Deserialize, Debug)]
struct AnimeItem {
    name: String,
    based: i32,
    age: i32,
    degen: i32,
    normie: i32,
    completion: i32,
    ranked: i32,
}

#[derive(Serialize, Deserialize, Debug)]
struct AnimeList {
    username: String,
    time_stamp: String,
    anime_list: Vec<AnimeItem>,
}

pub fn main() {
    // let file_path = "template.json";
    // let json_data = fs::read_to_string(file_path);

    let json_data = r#"
    {
        "username": "joe",
        "time_stamp": "9438204830",
        "anime_list": [
            {
                "name": "boku no pico",
                "based": 75,
                "age": 55,
                "degen": 100,
                "normie": 45,
                "completion": 60,
                "ranked": 30
            },
            {
                "name": "naruto",
                "based": 80,
                "age": 50,
                "degen": 70,
                "normie": 60,
                "completion": 85,
                "ranked": 40
            }
        ]
    }
    "#;

    let parsed_data: AnimeList = serde_json::from_str(&json_data).expect("Failed to parse JSON");

    let username = parsed_data.username;
    let count = parsed_data.anime_list.len() as f32;

    let total_based: i32 = parsed_data.anime_list.iter().map(|anime| anime.based).sum();
    let total_age: i32 = parsed_data.anime_list.iter().map(|anime| anime.age).sum();
    let total_degen: i32 = parsed_data.anime_list.iter().map(|anime| anime.degen).sum();
    let total_normie: i32 = parsed_data
        .anime_list
        .iter()
        .map(|anime| anime.normie)
        .sum();
    let total_completion: i32 = parsed_data
        .anime_list
        .iter()
        .map(|anime| anime.completion)
        .sum();
    let total_ranked: i32 = parsed_data
        .anime_list
        .iter()
        .map(|anime| anime.ranked)
        .sum();

    let average_based = (total_based as f32 / count) as u32;
    let average_age = (total_age as f32 / count) as u32;
    let average_degen = (total_degen as f32 / count) as u32;
    let average_normie = (total_normie as f32 / count) as u32;
    let average_completion = (total_completion as f32 / count) as u32;
    let average_ranked = (total_ranked as f32 / count) as u32;

    let score_list = ScoreListStruct {
        based: average_based,
        age: average_age,
        degen: average_degen,
        normie: average_normie,
        completion: average_completion,
        ranked: average_ranked,
    };

    let bytes = PublicValuesStruct::abi_encode(&PublicValuesStruct {
        username,
        time_stamp: parsed_data.time_stamp,
        score_list,
    });

    sp1_zkvm::io::commit_slice(&bytes);
}
