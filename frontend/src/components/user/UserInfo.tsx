

export default function UserInfo({image_url, info}) {


    return (
        <>
            <div className="flex flex-row items-center justify-center">
                <img src={image_url} className="w-1/4 h-1/4" />
                <div className="flex flex-col items-center justify-center">
                    {info}
                </div>
            </div>
        </>
    )
}