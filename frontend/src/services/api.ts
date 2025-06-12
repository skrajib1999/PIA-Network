const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export type UserProfile = {
  id: number;
  username: string;
  email: string;
  balance: number;
  referralsCount: number;
};

export type LeaderboardEntry = {
  id: number;
  username: string;
  totalMined: number;
  rank: number;
};

export type Task = {
  id: number;
  title: string;
  description?: string;
  reward: number;
  is_active: boolean;
};

async function handleResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    const errorData = await response.json().catch(() => null);
    throw new Error(errorData?.detail || response.statusText);
  }
  return response.json();
}

// Auth
export async function loginWithTelegram(token: string): Promise<{ access_token: string }> {
  const response = await fetch(`${API_BASE_URL}/auth/telegram-login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ token }),
  });
  return handleResponse(response);
}

export async function loginWithGoogle(token: string): Promise<{ access_token: string }> {
  const response = await fetch(`${API_BASE_URL}/auth/google-login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ token }),
  });
  return handleResponse(response);
}

// User Profile
export async function fetchUserProfile(token: string): Promise<UserProfile> {
  const response = await fetch(`${API_BASE_URL}/users/me`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return handleResponse(response);
}

// Leaderboard
export async function fetchLeaderboard(): Promise<LeaderboardEntry[]> {
  const response = await fetch(`${API_BASE_URL}/leaderboard`);
  return handleResponse(response);
}

// Tasks
export async function fetchTasks(): Promise<Task[]> {
  const response = await fetch(`${API_BASE_URL}/tasks`);
  return handleResponse(response);
}

// Mining
export async function mine(token: string): Promise<{ success: boolean; new_balance: number }> {
  const response = await fetch(`${API_BASE_URL}/mine`, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}` },
  });
  return handleResponse(response);
}

export default {
  loginWithTelegram,
  loginWithGoogle,
  fetchUserProfile,
  fetchLeaderboard,
  fetchTasks,
  mine,
};
