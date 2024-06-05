"""

This is a lil mock task that is represented of one of the many types of tasks you'll do.

The task is to implement compute_agent_response_times.

See the docstr of that function for more info.


"""

import pickle as pkl
from dataclasses import dataclass
from datetime import datetime


@dataclass
class metricRow:
    ticket_id: str
    agent_id: str
    metric_time: datetime
    metric_val: float


def load_sample_ticket_blocks():
    """utility to load the sample data.txt file into a list of ticket blocks"""
    with open("data.pkl", "rb") as f:
        blocks = pkl.load(f)
    assert len(blocks) == 10, "should have 10 ticket blocks in the file"
    return blocks


def compute_metrics():
    """ """
    blocks = load_sample_ticket_blocks()
    metrics = []
    for block in blocks:
        metrics = example_metric_count_of_agent_comments(block)
        # metrics = compute_agent_response_times(block)
        metrics.extend(metrics)

    return metrics


def compute_agent_response_times(ticket_bock: dict) -> list[metricRow]:
    """
    This function takes a "ticket block" which is a dict of a "ticket" and "comments".

    This represents a stub version of data you will work with at maestro, this represents
    1 customer service interaction - data our ETL system collects.


    https://docs.google.com/document/d/1MfcE7aZ6EXuyu2XeckdEg8mhib6yWeewK_TTSOJDAy8/edit
    """
    raise Exception("not implemented")


def example_metric_count_of_agent_comments(ticket_block: dict) -> list[metricRow]:
    """
    example metric - just a count of each agents comment on the ticket block.
    """
    return [
        metricRow(
            ticket_id=ticket_block["ticket"]["id"],
            agent_id=comment["author_id"],
            metric_time=comment["time"],
            metric_val=1.0,
        )
        for comment in ticket_block["comments"]
        if comment["author_type"] == "agent"
    ]


if __name__ == "__main__":
    ms = compute_metrics()
    print(ms)
