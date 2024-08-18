import { useEffect, useState } from "react"
import UserInfo from "../components/user/UserInfo"


export default function UserPage() {
    
    const [userData, setUserData] = useState<any | null>(null)
    const [isLoading, setIsLoading] = useState<boolean>(true)
    

    useEffect(() => {
        setIsLoading(true)
        async function getUserData() {
            const data = {
                "image_url": "kladsjf;lkds",
                "info": {
                    "name": "name"
                }
            }
        
            setUserData(data)
            setIsLoading(false)
        }

        getUserData()
    }, [])

    if (userData) {
        return (
            <UserInfo image_url={userData.image_url} info={userData.info} />
        )
    } else {
        return (
            <></>
        )
    }
}


