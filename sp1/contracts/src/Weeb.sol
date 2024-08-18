// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ISP1Verifier} from "@sp1-contracts/ISP1Verifier.sol";

struct PublicValuesStruct {
    string username;
    string timestamp;
    uint128[] scoreList;
}

/// @title Fibonacci.
/// @author Succinct Labs
/// @notice This contract implements a simple example of verifying the proof of being a weeb.
contract Weeb {
    /// @notice The address of the SP1 verifier contract.
    address public verifier;

    /// @notice The verification key for the weeb program.
    bytes32 public weebProgramVKey;

    constructor(address _verifier, bytes32 _weebProgramVKey) {
        verifier = _verifier;
        weebProgramVKey = _weebProgramVKey;
    }

    /// @notice The entrypoint for verifying the proof of a weeb.
    /// @param _proofBytes The encoded proof.
    /// @param _publicValues The encoded public values.
    function verifyFibonacciProof(
        bytes calldata _publicValues,
        bytes calldata _proofBytes
    ) public view returns (string memory, string memory, uint128[] memory) {
        ISP1Verifier(verifier).verifyProof(
            weebProgramVKey,
            _publicValues,
            _proofBytes
        );
        PublicValuesStruct memory publicValues = abi.decode(
            _publicValues,
            (PublicValuesStruct)
        );
        return (
            publicValues.username,
            publicValues.timestamp,
            publicValues.scoreList
        );
    }
}
