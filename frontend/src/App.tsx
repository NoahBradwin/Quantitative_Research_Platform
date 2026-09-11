import type { ChangeEvent } from "react";

async function handleFileChange(event: ChangeEvent<HTMLInputElement>) {
  const file = event.currentTarget.files?.[0]

  if (!file) {
    return
  }

  const text = await file.text();
  console.log(text);
}

function App() {
  return (
    <main>
      <input type="file" accept=".csv" onChange={handleFileChange} />
    </main>
  )
}

export default App;

