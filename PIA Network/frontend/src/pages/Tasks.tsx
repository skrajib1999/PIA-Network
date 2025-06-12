import React, { useEffect, useState } from "react";

type Task = {
  id: number;
  title: string;
  description?: string;
  reward: number;
  is_active: boolean;
};

const Tasks: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Simulate fetching tasks from API
    const fetchTasks = async () => {
      setLoading(true);
      try {
        const data: Task[] = [
          {
            id: 1,
            title: "Share on Social Media",
            description: "Share PIA Network on your social media to earn rewards.",
            reward: 50,
            is_active: true,
          },
          {
            id: 2,
            title: "Complete Profile",
            description: "Fill out your profile information to get a bonus.",
            reward: 30,
            is_active: true,
          },
          {
            id: 3,
            title: "Invite a Friend",
            description: "Invite a friend to join and earn referral rewards.",
            reward: 100,
            is_active: false,
          },
        ];
        setTasks(data);
      } catch (error) {
        console.error("Failed to fetch tasks:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6 text-center">Tasks</h1>

      {loading ? (
        <p className="text-center">Loading tasks...</p>
      ) : tasks.length === 0 ? (
        <p className="text-center text-gray-600 dark:text-gray-400">No active tasks available.</p>
      ) : (
        <ul className="space-y-4 max-w-3xl mx-auto">
          {tasks.map(({ id, title, description, reward, is_active }) => (
            <li
              key={id}
              className={`p-6 rounded-lg shadow-md border ${
                is_active
                  ? "bg-white dark:bg-gray-800 border-gray-300 dark:border-gray-700"
                  : "bg-gray-100 dark:bg-gray-700 border-gray-200 dark:border-gray-600 opacity-60 cursor-not-allowed"
              }`}
            >
              <h2 className="text-xl font-semibold mb-1">{title}</h2>
              {description && <p className="text-gray-600 dark:text-gray-300 mb-3">{description}</p>}
              <p className="font-medium text-green-600 dark:text-green-400">Reward: {reward} PIA</p>
              {!is_active && <p className="text-sm text-red-500 mt-2">Task inactive</p>}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Tasks;
