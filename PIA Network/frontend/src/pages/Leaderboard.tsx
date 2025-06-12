import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface UserProfile {
  id: number;
  email: string;
  full_name?: string;
  created_at: string;
  total_mined: number;
  mining_power: number;
}

const Profile: React.FC = () => {
  const [user, setUser] = useState<UserProfile | null>(null);
  const [loading, setLoading] = useState(true);

  const fetchProfile = async () => {
    try {
      const res = await axios.get(`${import.meta.env.VITE_API_BASE_URL}/user/me`, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      });
      setUser(res.data);
    } catch (err) {
      console.error('Failed to fetch profile', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProfile();
  }, []);

  if (loading) {
    return <div className="text-center mt-10">Loading profile...</div>;
  }

  if (!user) {
    return <div className="text-center mt-10 text-red-500">User not found or unauthorized.</div>;
  }

  return (
    <div className="max-w-3xl mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6">Your Profile</h1>
      <div className="bg-white dark:bg-gray-800 shadow rounded-2xl p-6 space-y-4">
        <div>
          <p className="text-sm text-gray-500">Email</p>
          <p className="text-lg font-medium">{user.email}</p>
        </div>
        {user.full_name && (
          <div>
            <p className="text-sm text-gray-500">Full Name</p>
            <p className="text-lg font-medium">{user.full_name}</p>
          </div>
        )}
        <div>
          <p className="text-sm text-gray-500">Account Created</p>
          <p className="text-lg font-medium">{new Date(user.created_at).toLocaleString()}</p>
        </div>
        <div className="border-t pt-4">
          <p className="text-sm text-gray-500">Total Mined</p>
          <p className="text-2xl font-semibold text-indigo-600 dark:text-indigo-400">{user.total_mined.toFixed(4)} PIA</p>
        </div>
        <div>
          <p className="text-sm text-gray-500">Mining Power</p>
          <p className="text-xl font-medium">{user.mining_power.toFixed(2)}x</p>
        </div>
      </div>
    </div>
  );
};

export default Profile;
