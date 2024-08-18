import axios from "axios";
import { useEffect } from "react";



export default function PersonalPage() {

    const [jwt, setJWT] = useState<string | null>(null);

    useEffect(() => {
        setJWT(getJWTToken());
    }, [])


    async function handleGenerate() {
        const response = await axios.get('http://localhost:3000/api/generate', {
            headers: {
                Authorization: `Bearer ${jwt}`
            }
        });
    }

    if (!jwt) {
        return (
            <h1>Not logged in</h1>
        )
    } else {
        return (
            <div>
                <h1>Logged in</h1>
                <button onClick={handleGenerate}>Generate</button>
            </div>
        )
    }

}

function getJWTToken() {
    return localStorage.getItem('jwt');
}