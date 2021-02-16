library(tidyverse)

df <- read_csv("epa-sea-level.csv")

# Create a scatterplot with x="Year" and y="CSIRO Adjusted Sea Level"
# Add the line of best fit, predicting up to year 2050
p <- df %>%
    ggplot(aes(x = Year, y = `CSIRO Adjusted Sea Level`)) +
    geom_point() +
    xlim(1880, 2050) +
    ylim(0.0, 15.0) +
    stat_smooth(
        method = "lm",
        size = 1,
        color = "red",
        se = FALSE,
        fullrange = TRUE
    )

# Recalculate the line of best fit using just data from 2000-2013
df_subset <- df[df$Year >= 2000, ]

fit_subset <- lm(`CSIRO Adjusted Sea Level` ~ Year, data = df_subset)

int <- coef(fit_subset)[1]
slope <- coef(fit_subset)[2]

# Add second best fit line to the scatter plot, predicting up to year 2050
p + geom_abline(slope = slope, intercept = int, color = "blue", size = 1) +
    labs(x = "Year", y = "Sea Level (inches)", title = "Rise in Sea Level") +
    theme(plot.title = element_text(hjust = 0.5)) +
    annotate(
        geom = "text",
        label = "Fitted line using only the years after 2000",
        x = 2025,
        y = 15,
        color = "blue"
    ) +
    annotate(
        geom = "text",
        label = "Fitted line using all years",
        x = 2045,
        y = 10.5,
        color = "red"
    )