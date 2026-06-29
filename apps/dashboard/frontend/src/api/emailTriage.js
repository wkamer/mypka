import { api } from "./client";

export const emailTriageApi = {
  runTriage: () => api.post("/api/email-management/run", {}),
  getEmails: () => api.get("/api/email-management/emails"),
  getActions: (emailId) =>
    api.get(`/api/email-management/emails/${emailId}/actions`),
  patchAction: (actionId, body) =>
    api.patch(`/api/email-management/actions/${actionId}`, body),
  createAction: (emailId, body) =>
    api.post(`/api/email-management/emails/${emailId}/actions`, body),
};
