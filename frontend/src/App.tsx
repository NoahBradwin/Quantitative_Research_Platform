import type { ChangeEvent } from "react";
import { useState } from "react";



function App() {

  const[rows, setRows] = useState<string[][]>([]);

  async function handleFileChange(event: ChangeEvent<HTMLInputElement>) {
    const file = event.currentTarget.files?.[0]

    if (!file) {
      return
    }

    const text = await file.text();
    setRows(text.trim().split(/\r?\n/).map((line) => line.split(",")));

  }

  return (
    <main>
      <input type="file" accept=".csv" onChange={handleFileChange} />
      <table>
        <thead>
          <tr>
            {rows[0]?.map((heading, index) => (<th key={index}>{heading}</th>))}
          </tr>
        </thead>

        <tbody>
          {rows.slice(1,6).map((row, rowIndex) => (<tr key={rowIndex}>{row.map((cell, columnIndex) => (<td key={columnIndex}>{cell}</td>))}</tr>))}
        </tbody>
      </table>
    </main>
  )
}

export default App;

