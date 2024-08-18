import { useEffect, useState } from "react"
import UserInfo from "../components/user/UserInfo"


export default function UserPage() {
    
    const [userData, setUserData] = useState<any | null>(null)

    useEffect(() => {
        getUserData(setUserData)
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


async function getUserData(setFn) {
    let data = {
        "image_url": "kladsjf;lkds",
        "info": {
            "name": "name"
        }
    }

    setFn(data)
}