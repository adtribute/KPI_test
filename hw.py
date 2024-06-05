"""

This is a lil mock task that is representative of one of the many types of tasks you'll do at maestro!

The task is to implement compute_agent_response_times.

See the docstr of that function for more info.
"""

import pickle as pkl
from dataclasses import dataclass
from datetime import datetime


@dataclass
class metricRow:
    """the function you are implementing should return a list of these,
    these represent metric rows that would be loaded into our reporting
    system to power our customers dashboards and reports.
    """

    ticket_id: str
    agent_id: str
    metric_time: datetime
    metric_val: float


def compute_metrics():
    """this is the main function that loaded the sample data and executes
    the compute_agent_response_times function on each block of tickets to
    produce metric rows.
    """
    with open("data.pkl", "rb") as f:
        blocks = pkl.load(f)
    assert len(blocks) == 10, "should have 10 ticket blocks in the file"

    metrics = []
    for block in blocks:
        # metrics = example_metric_count_of_agent_comments(block)
        metrics = compute_agent_response_times(block)
        metrics.extend(metrics)

    return metrics


def compute_agent_response_times(ticket_bock: dict) -> list[metricRow]:
    """
    This function takes a "ticket block" which is a dict of a "ticket" and "comments".

    This is a simplified version of data you will work with at maestro, this represents
    1 customer service interaction - data our ETL system collects.

    This function implements the logic of a common type of 'metric'  our customers use -
    agent response times.

    This is basically just the delta in time from a customers message til the agents response.

    However there are a few subleties:
        - these chats sometimes starts with a bot interaction. either way, the clock
          doesnt start till the agent joins. the first agent response time is the time
          from the agent joining the chat, til thier next message.

         - the customer or agent can send multiple chats right after each other, without
          the other person messaging. In this case we only care about the time of the
          first message.

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
    for m in ms:
        print(m)
