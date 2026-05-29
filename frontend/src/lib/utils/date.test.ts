import { describe, expect, it } from "vitest";

import {
  formatDateTime,
  formatDueDate,
  formatTableDate,
  isDateFuture,
  isDatePast,
} from "./date";

describe("date utilities", () => {
  it("returns display fallbacks for empty dates", () => {
    expect(formatDateTime(null)).toBe("—");
    expect(formatTableDate(undefined)).toBe("—");
    expect(formatDueDate(null)).toEqual({
      formatted: "No due date",
      status: "none",
      isOverdue: false,
      isUrgent: false,
    });
  });

  it("normalizes date strings without timezone information", () => {
    expect(formatDateTime("2026-06-01", false)).toMatch(/2026$/);
    expect(formatTableDate("2026-06-01 12:30:00")).toMatch(/\d{1,2}\/\d{1,2}\/26/);
  });

  it("classifies past and future dates", () => {
    expect(isDatePast("1970-01-01T00:00:00Z")).toBe(true);
    expect(isDateFuture("2999-01-01T00:00:00Z")).toBe(true);
  });
});
