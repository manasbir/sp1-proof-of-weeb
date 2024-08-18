import axios from "axios";
import { useEffect, useState } from "react";
import Loading from "./Loading";



export default function PersonalPage() {

    const [jwt, setJWT] = useState<string | null>(null);

    const [isLoading, setIsLoading] = useState<boolean>(true);
    const [isGenerating, setIsGenerating] = useState<boolean>(false);
    const [data, setData] = useState<any | null>(null);

    useEffect(() => {

    async function fetchInfo() {
        setIsLoading(true)
        const res = await axios.post(
            'http://localhost:3000/api/fetch',
            {
                headers: {
                    Authorization: `Bearer ${jwt}`
                }
            }
        )

        setData(res.data);
    }
        setJWT(getJWTToken());
        fetchInfo();
    }, [])


    async function handleGenerate() {
        setIsGenerating(true);
        const response = await axios.get('http://localhost:3000/api/generate', {
            headers: {
                Authorization: `Bearer ${jwt}`
            }
        });
        window.open(window.location.origin + "/user/" + response.data)
    }


    if (!jwt) {
        return (
            <h1>Not logged in</h1>
        )
    } else {
        if (isLoading) {
            return (
                <div>
                    <Loading />
                </div>
            )
        } else {
            if (isGenerating) {
                return (
                    <div>
                        <h1>Generating</h1>
                        <Loading />
                    </div>
                )
            }
            if (data) {
                return (
                    <div>
                        <h1>Generated</h1>
                        <div>{data}</div>
                    </div>
                )
            } else {
                return (
                    <div>
                        <h1>Not generated</h1>
                        <button onClick={handleGenerate}>Generate</button>
                    </div>
                )
            }
        }
    }

}

function getJWTToken() {
    return localStorage.getItem('jwt');
}