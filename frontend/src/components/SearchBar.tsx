import { useState } from "react";


export default function SearchBar() {
    const [search, setSearch] = useState("");

    const onFormSubmit = (e: any) => {
        e.preventDefault();
        window.open(window.location.origin + "/user/" + search)!.focus();

    }


    return (
        <div>
            <form className="" onSubmit={onFormSubmit}>
                <input onChange={e => setSearch(e.currentTarget.value)} type="text" placeholder="Search" value={search}></input>
                <button className="" type="submit">Submit</button>
            </form>

        </div>
    )
}