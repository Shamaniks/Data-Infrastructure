ERRORS = {
    "NO_TOKEN": ("Authorization token is missing", 401),
    "INVALID_TOKEN": ("Token is invalid or expired", 401),
    "WRONG_CREDENTIALS": ("Invalid login or password", 401),
    "ACCESS_DENIED": ("Database access denied for this role", 403),
    "SERVER_ERROR": ("Oh no (Internal server error)", 500),
    "BAD_REQUEST": ("Invalid request format", 400),
    "TABLE_NOT_FOUND": ("The requested table does not exist", 404),
}
