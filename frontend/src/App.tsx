import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ThemeProvider } from "@/components/theme-provider"; // Optional: theme context
import Navbar from "@/components/Navbar";

// Pages
import Home from "@/pages/Home";
import Profile from "@/pages/Profile";
import Leaderboard from "@/pages/Leaderboard";
import Tasks from "@/pages/Tasks";

const App: React.FC = () => {
  return (
    <Router>
      <ThemeProvider>
        <div className="min-h-screen bg-white text-gray-900 dark:bg-gray-900 dark:text-white transition-colors duration-300">
          <Navbar />
          <main className="max-w-7xl mx-auto p-4">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/profile" element={<Profile />} />
              <Route path="/leaderboard" element={<Leaderboard />} />
              <Route path="/tasks" element={<Tasks />} />
              {/* Optional: 404 route */}
              <Route path="*" element={<div className="text-center mt-20 text-xl">Page Not Found</div>} />
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </Router>
  );
};

export default App;
