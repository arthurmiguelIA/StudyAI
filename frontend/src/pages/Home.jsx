import { useState } from "react";
import { api } from "../services/api";

export default function Home() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    setLoading(true);

    const res = await api.post("/materials/", {
      text: text
    });

    setResult(res.data);
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-gray-800 flex items-center justify-center p-6">

      <div className="w-full max-w-3xl bg-white/5 backdrop-blur-lg p-6 rounded-2xl shadow-xl border border-white/10">

        <h1 className="text-3xl font-bold text-white mb-4">
          📚 StudyAI
        </h1>

        <textarea
          className="w-full p-4 rounded-xl bg-gray-900 text-white border border-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
          placeholder="Digite ou cole um texto para gerar resumo..."
          rows={5}
          onChange={(e) => setText(e.target.value)}
        />

        <button
          onClick={handleGenerate}
          className="mt-4 w-full bg-blue-600 hover:bg-blue-500 transition text-white py-3 rounded-xl font-semibold flex justify-center items-center gap-2"
        >
          {loading ? "Gerando..." : "Gerar resumo"}
        </button>

        {result && (
          <div className="mt-6 p-4 bg-gray-900 rounded-xl border border-gray-700 animate-fade-in">

            <h2 className="text-xl font-semibold text-blue-400 mb-2">
              ✨ Resumo
            </h2>

            <p className="text-gray-300 leading-relaxed">
              {result.summary}
            </p>

          </div>
        )}
      </div>
    </div>
  );
}