use alloy_sol_types::sol;
use serde::Serialize;

sol! {
    #[derive(Debug, Serialize)]
    struct ScoreListStruct {
        uint32 based;
        uint32 age;
        uint32 degen;
        uint32 normie;
        uint32 completion;
        uint32 ranked;
    }
}

sol! {
    #[derive(Debug, Serialize)]
    struct PublicValuesStruct {
        string username;
        string time_stamp;
        ScoreListStruct score_list;
    }
}
