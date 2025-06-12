import React from "react";
import { Link } from "react-router-dom";
import MinerCard from "@/components/MinerCard";

const Home: React.FC = () => {
  return (
    <div className="flex flex-col gap-8">
      <section className="text-center">
        <h1 className="text-4xl font-bold mb-4">Welcome to PIA Network</h1>
        <p className="text-lg text-gray-600 dark:text-gray-300">
          Simulate crypto mining, earn rewards, and climb the leaderboard.
        </p>
      </section>

      <section>
        <h2 className="text-2xl font-semibold mb-4">Start Mining</h2>
        <MinerCard />
      </section>

      <section className="grid grid-cols-1 sm:grid-cols-2 gap-6">
        <div className="p-6 bg-primary text-white rounded-2xl shadow-md">
          <h3 className="text-xl font-semibold mb-2">Check Your Profile</h3>
          <p className="mb-4">Track your progress, wallet balance, and referrals.</p>
          <Link to="/profile" className="underline text-sm">Go to Profile →</Link>
        </div>
        <div className="p-6 bg-secondary text-white rounded-2xl shadow-md">
          <h3 className="text-xl font-semibold mb-2">Complete Tasks</h3>
          <p className="mb-4">Earn extra rewards by completing tasks and missions.</p>
          <Link to="/tasks" className="underline text-sm">View Tasks →</Link>
        </div>
      </section>
    </div>
  );
};

export default Home;
