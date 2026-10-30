INSERT INTO SchemaVersion(version_number, date_applied) VALUES ('1.1', 'Sep-19-2025');

CREATE TABLE Movies (
    movieId VARCHAR PRIMARY KEY,
    movie VARCHAR NOT NULL,
    release_year INT,
    director VARCHAR,
    genre VARCHAR,
    quoteId VARCHAR,
    FOREIGN KEY (quoteId) REFERENCES Quotes(quoteId),
    UNIQUE (movieId)
);

CREATE INDEX idx_movie ON Movies(movie);

CREATE TABLE Quotes (
    quoteId VARCHAR PRIMARY KEY,
    quote VARCHAR NOT NULL,
    movieId VARCHAR NOT NULL,
    FOREIGN KEY (movieId) REFERENCES Movies(movieId),
    UNIQUE (quoteId)
);

CREATE INDEX idx_quote ON Quotes(quote);