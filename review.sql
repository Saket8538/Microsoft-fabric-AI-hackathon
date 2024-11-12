-- Create the CustomerReviews table
CREATE TABLE CustomerReviews (
    ReviewID INT PRIMARY KEY IDENTITY(1,1),  -- Auto-incrementing primary key
    ReviewText NVARCHAR(MAX),                -- Text of the customer review
    Sentiment NVARCHAR(50)                   -- Sentiment of the review (e.g., Positive, Negative, Neutral)
);
CREATE INDEX idx_sentiment ON CustomerReviews(Sentiment);
SELECT ReviewText, Sentiment
FROM CustomerReviews
WHERE Sentiment = 'Positive';
/* Insert sample data into the CustomerReviews table */
SELECT Sentiment, COUNT(*) AS ReviewCount
FROM CustomerReviews
GROUP BY Sentiment;

DECLARE @PageNumber AS INT, @RowsPerPage AS INT;
SET @PageNumber = 1;
SET @RowsPerPage = 10;

WITH ReviewsCTE AS
(
    SELECT ROW_NUMBER() OVER (ORDER BY ReviewID) AS RowNum, ReviewText, Sentiment
    FROM CustomerReviews
)
SELECT ReviewText, Sentiment
FROM ReviewsCTE
WHERE RowNum BETWEEN ((@PageNumber - 1) * @RowsPerPage + 1) AND (@PageNumber * @RowsPerPage);