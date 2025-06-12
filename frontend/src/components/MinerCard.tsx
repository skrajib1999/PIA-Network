import React, { useState, useEffect } from "react";

type MinerCardProps = {
  miningRate?: number; // e.g., PIA per hour
  balance?: number; // current mined balance
  lastMinedAt?: string; // ISO timestamp of last mining event
  onMine?: () => Promise<void>; // function to trigger mining
};

const MinerCard: React.FC<MinerCardProps> = ({
  miningRate = 10,
  balance = 0,
  lastMinedAt,
  onMine,
}) => {
  const [loading, setLoading] = useState(false);
  const [lastMined, setLastMined] = useState<Date | null>(lastMinedAt ? new Date(lastMinedAt) : null);

  const handleMine = async () => {
    if (!onMine) return;
    setLoading(true);
    try {
      await onMine();
      setLastMined(new Date());
    } catch (error) {
      console.error("Mining failed:", error);
    } finally {
      setLoading(false);
    }
  };

  const getTimeSinceLastMine = () => {
    if (!lastMined) return "Never";
    const diffMs = Date.now() - lastMined.getTime();
    const diffMins = Math.floor(diffMs / 60000);
    if (diffMins < 1) return "Just now";
    if (diffMins < 60) return `${diffMins} min ago`;
    const diffHours = Math.floor(diffMins / 60);
    if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? "s" : ""} ago`;
    const diffDays = Math.floor(diffHours / 24);
    return `${diffDays} day${diffDays > 1 ? "s" : ""} ago`;
  };

  return (
    <div className="max-w-md mx-auto bg-white dark:bg-gray-800 shadow-lg rounded-2xl p-6 text-center">
      <h3 className="text-2xl font-bold mb-4">Simulated Miner</h3>
      <p className="text-gray-700 dark:text-gray-300 mb-2">
        Mining Rate: <span className="font-semibold">{miningRate} PIA/hour</span>
      </p>
      <p className="text-gray-700 dark:text-gray-300 mb-4">
        Current Balance: <span className="font-semibold">{balance.toFixed(2)} PIA</span>
      </p>
      <p className="text-sm text-gray-500 dark:text-gray-400 mb-6">
        Last mined: {getTimeSinceLastMine()}
      </p>
      <button
        onClick={handleMine}
        disabled={loading}
        className={`px-6 py-3 rounded-full font-semibold text-white transition-colors ${
          loading
            ? "bg-gray-400 cursor-not-allowed"
            : "bg-indigo-600 hover:bg-indigo-700 dark:bg-indigo-500 dark:hover:bg-indigo-600"
        }`}
      >
        {loading ? "Mining..." : "Mine Now"}
      </button>
    </div>
  );
};

export default MinerCard;

<MinerCard
  miningRate={12}
  balance={123.45}
  lastMinedAt="2025-06-11T12:00:00Z"
  onMine={async () => {
    // Call backend mine endpoint
    await fetch("/api/mine", { method: "POST" });
  }}
/>
