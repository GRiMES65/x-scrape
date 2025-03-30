"use client";
import { useState, useEffect } from "react";

interface TwitterResponse {
  error?: string;
  text?: string;
  sentiment?: string;
}

export default function Home() {
  const [username, setUsername] = useState("");
  const [results, setResults] = useState<
    Array<{ text: string; sentiment: string }>
  >([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [loadingStage, setLoadingStage] = useState(0);

  // Add loading animation interval
  useEffect(() => {
    let interval: NodeJS.Timeout;
    if (loading) {
      interval = setInterval(() => {
        setLoadingStage((prev) => (prev + 1) % 4);
      }, 500);
    }
    return () => clearInterval(interval);
  }, [loading]);

  const getLoadingMessage = () => {
    const stages = [
      "🤔 Analyzing tweets...",
      "😊 Finding positive vibes...",
      "😠 Detecting negativity...",
      "😐 Measuring neutrality...",
    ];
    return stages[loadingStage];
  };

  const analyzeSentiment = async () => {
    setLoading(true);
    setError("");
    setResults([]);

    try {
      const response = await fetch(
        `https://tweet-mood.onrender.com/analyze/twitter?username=${username}`
      );
      const data: TwitterResponse[] = await response.json();

      if (!response.ok) {
        setError(data[0]?.error || "Failed to analyze tweets");
        return;
      }

      if (Array.isArray(data) && data.length === 0) {
        setError("No tweets found for this username");
        return;
      }

      setResults(data as Array<{ text: string; sentiment: string }>);
    } catch (err) {
      setError("Failed to fetch results. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  // Calculate sentiment counts from results
  const sentimentCounts = {
    Positive: results.filter((r) => r.sentiment === "Positive").length,
    Negative: results.filter((r) => r.sentiment === "Negative").length,
    Neutral: results.filter((r) => r.sentiment === "Neutral").length,
  };

  const totalAnalyzed = results.length;
  const positivePercentage = totalAnalyzed
    ? ((sentimentCounts.Positive / totalAnalyzed) * 100).toFixed(1)
    : 0;
  const negativePercentage = totalAnalyzed
    ? ((sentimentCounts.Negative / totalAnalyzed) * 100).toFixed(1)
    : 0;

  const getSentimentSummary = () => {
    if (!totalAnalyzed) return "";
    if (sentimentCounts.Positive > sentimentCounts.Negative * 1.5) {
      return "Overwhelmingly Positive";
    } else if (sentimentCounts.Positive > sentimentCounts.Negative) {
      return "Generally Positive";
    } else if (sentimentCounts.Negative > sentimentCounts.Positive * 1.5) {
      return "Overwhelmingly Negative";
    } else if (sentimentCounts.Negative > sentimentCounts.Positive) {
      return "Generally Negative";
    }
    return "Neutral/Mixed";
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8 px-4 sm:px-6 lg:px-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-3xl font-bold text-center mb-8 text-gray-900 ">
          TweetMood Sentiment Analyzer
        </h1>

        <div className="flex gap-6">
          <div className="flex-1">
            <div className="bg-white p-6 rounded-lg shadow-sm mb-6 transition-all duration-300 hover:shadow-lg">
              <div className="flex gap-4 mb-4">
                <input
                  type="text"
                  placeholder="Enter username"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  className="flex-1 px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-400 transition-all duration-200 hover:border-blue-400"
                />
                <button
                  onClick={analyzeSentiment}
                  disabled={loading || !username}
                  className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 hover:cursor-pointer transition-all duration-400 transform hover:scale-102 active:scale-95"
                >
                  Analyze User
                </button>
              </div>

              {loading && (
                <div className="text-center py-8 animate-pulse text-gray-700">
                  <div className="text-2xl mb-2 text-gray-700">{getLoadingMessage()}</div>
                  <div className="text-sm text-gray-700">
                    Analyzing @{username}'s Twitter vibe...
                  </div>
                </div>
              )}

              {error && (
                <div className="text-red-500 text-center mb-4 transition-all duration-300 animate-fade-in">
                  {error}
                </div>
              )}

              {results.length > 0 && (
                <div className="space-y-4">
                  {results.map((result, index) => (
                    <div
                      key={index}
                      className="p-4 rounded-lg border border-gray-200 transition-all duration-300 hover:shadow-md hover:border-gray-300 transform hover:-translate-y-1"
                    >
                      <p className="text-gray-700">{result.text}</p>
                      <span
                        className={`inline-block mt-2 px-2 py-1 text-sm rounded transition-colors duration-200 ${
                          result.sentiment === "Positive"
                            ? "bg-green-100 text-green-800 hover:bg-green-200"
                            : result.sentiment === "Negative"
                            ? "bg-red-100 text-red-800 hover:bg-red-200"
                            : "bg-gray-100 text-gray-800 hover:bg-gray-200"
                        }`}
                      >
                        {result.sentiment}
                      </span>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          {results.length > 0 && (
            <div className="w-64 transition-transform duration-300 transform translate-x-0">
              <div className="bg-white p-6 rounded-lg shadow-sm transition-all duration-300 hover:shadow-lg">
                <h3 className="text-lg font-semibold mb-4 text-gray-900">
                  Sentiment Analysis
                </h3>
                <div className="space-y-4">
                  <div className="p-4 bg-green-50 rounded-lg">
                    <div className="text-2xl font-bold text-green-600">
                      {sentimentCounts.Positive}
                    </div>
                    <div className="text-sm text-green-800">Positive</div>
                  </div>
                  <div className="p-4 bg-red-50 rounded-lg">
                    <div className="text-2xl font-bold text-red-600">
                      {sentimentCounts.Negative}
                    </div>
                    <div className="text-sm text-red-800">Negative</div>
                  </div>
                  <div className="p-4 bg-gray-50 rounded-lg">
                    <div className="text-2xl font-bold text-gray-600">
                      {sentimentCounts.Neutral}
                    </div>
                    <div className="text-sm text-gray-800">Neutral</div>
                  </div>
                </div>
              </div>

              <div className="bg-white p-6 rounded-lg shadow-sm mt-4 transition-all duration-300 hover:shadow-lg">
                <h3 className="text-lg font-semibold mb-4 text-gray-900">
                  Overall Summary
                </h3>
                <div className="space-y-4">
                  <div className="text-sm text-gray-600">
                    Total Analyzed:{" "}
                    <span className="font-semibold">{totalAnalyzed}</span>
                  </div>
                  <div className="space-y-2">
                    <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-green-500 transition-all duration-1000 ease-out"
                        style={{ width: `${positivePercentage}%` }}
                      />
                    </div>
                    <div className="text-sm text-gray-600">
                      {positivePercentage}% Positive
                    </div>
                  </div>
                  <div className="space-y-2">
                    <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-red-500 transition-all duration-1000 ease-out"
                        style={{ width: `${negativePercentage}%` }}
                      />
                    </div>
                    <div className="text-sm text-gray-600">
                      {negativePercentage}% Negative
                    </div>
                  </div>
                  <div
                    className={`text-center p-2 rounded-lg font-medium transition-colors duration-300 ${
                      getSentimentSummary().includes("Positive")
                        ? "bg-green-50 text-green-800 hover:bg-green-100"
                        : getSentimentSummary().includes("Negative")
                        ? "bg-red-50 text-red-800 hover:bg-red-100"
                        : "bg-gray-50 text-gray-800 hover:bg-gray-100"
                    }`}
                  >
                    {getSentimentSummary()}
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
