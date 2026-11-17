# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []

    i = 1  # ==== yukari_paradise1 ====
    if i not in disabled_events:
        event_name = f"yukari_paradise{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "01_yuka-para_s.png",
                [
                    Source(
                        "https://web.archive.org/web/20161030214306/http://ttc.ninja-web.net/vo-para/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="ゆかパラ　チラシ絵：けっきー 様（月影）",
            ),
            Medium(
                "https://web.archive.org/web/20160910013726/http://ttc.ninja-web.net/vo-para/161002_layout.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20160910013726/http://ttc.ninja-web.net/vo-para/161002_layout.pdf",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 イベントホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20161030214306/http://ttc.ninja-web.net/vo-para/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=[
                "ゆかりPARADISE",
                "Yukari PARADISE",
                "ゆかりPARADISE1",
                "Yukari PARADISE 1",
                "ゆかパラ",
                "yuka-para 1",
            ],
            dates="2016.10.02",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20161030214306/http://ttc.ninja-web.net/vo-para/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20161104125219/http://ttc.ninja-web.net/vo-para/vo-para11_list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with VOCALOID PARADISE 11, モジュールPARADISE２, カゲロウパラダイス２, ツインテールカーニバル８, 制服宣言 and ずんだぱ～てぃ３（み!）",
            # comments=None,
            last_edited="2026.11.17",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== yukari_paradise2 ====
    if i not in disabled_events:
        event_name = f"yukari_paradise{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "02_DMH_NikVoAAYX70.png",
                [
                    Source(
                        "https://x.com/vo_para/status/919296450164428800",
                        (RT.Reliable, OT.OfficialExt),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1316493, 136.895784),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 イベントホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20171218024106/http://ttc.ninja-web.net/vo-para/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWktkJOUF1Dj75m5uf1NOu4f4ZSJqePSniPmQ-lFQLZKHHxYlMXIXqwIYRDL1Pz6uwvqNAVoxKFi8CsA2ShNX_STmUZUEoRQOhzKg37OkNQAgQS_TmjI_P2eocrZPK8YLDcj5hIMRA=s0?imgmax=0",
                url="https://maps.app.goo.gl/ZKEKnswpsBoZELkp6",
            ),
        ]
        event = Event(
            aliases=[
                "ゆかりPARADISE2",
                "Yukari PARADISE 2",
                "ゆかパラ2",
                "yuka-para 2",
            ],
            dates="2017.10.15",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20171218024106/http://ttc.ninja-web.net/vo-para/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20171218160152/http://ttc.ninja-web.net/vo-para/vo-para12_list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with VOCALOID PARADISE 12, レンミクPARADISE, カゲロウパラダイス３, 艦隊ぱれーど and 教えて！練習巡洋艦",
            # comments=None,
            last_edited="2026.11.17",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== yukari_paradise3 ====
    if i not in disabled_events:
        event_name = f"yukari_paradise{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "03_vo-para13.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20190211185119/http://ttc.ninja-web.net/vo-para/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="カタログ表紙イラスト　椎奈そあら様（月見野番士）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 白鳥ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20190211185119/http://ttc.ninja-web.net/vo-para/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=[
                "ゆかりPARADISE3",
                "Yukari PARADISE 3",
                "ゆかパラ3",
                "yuka-para 3",
            ],
            dates="2018.09.16",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20190211185119/http://ttc.ninja-web.net/vo-para/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20190307125920/http://ttc.ninja-web.net/vo-para/vo-para13_list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with VOCALOID PARADISE 13, AHS PARADISE and カイミクPARADISE",
            # comments=None,
            last_edited="2026.11.17",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 4  # ==== yukari_paradise4 ====
    if i not in disabled_events:
        event_name = f"yukari_paradise{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.334103, 137.1288233),
                address="Japan, 〒507-0831 Gifu, Tajimi, Shinmachi, 1 Chome−２３",
                description="多治見市産業文化センター ５階ホール (CANCELLED)",
                sources=[
                    Source(
                        "https://web.archive.org/web/20240714193723/http://ttc.ninja-web.net/vo-para/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkSZuwNxFhmlk_wbB5TDxN1XQ33eBXjMchn6XpudPnnmfnYGW-1Ik4UqKwx05HvOK3hm7_ry8bDbf8ZrrO3pZXIgd_0FAnI-WPdGWIfhiv8vRSXNboVBmnbFgP0FXuO62tPYsg8GQ=s812-k-no",
                url="https://maps.app.goo.gl/vQXSpphcMZdTU78u5",
            ),
        ]
        event = Event(
            aliases=[
                "ゆかりあかりPARADISE",
                "ゆかあかパラ",
                "yuka-aka-para",
                "結月ゆかり・紲星あかりオンリー",
                "ゆかりPARADISE4",
                "Yukari PARADISE 4",
                "ゆかパラ4",
                "yuka-para 4",
            ],
            dates="2019.10.20 → CANCELLED",
            circles=[],
            media=media_,
            sources=[
                Source(
                    'Alias "結月ゆかり・紲星あかりオンリー": https://web.archive.org/web/20240714193723/http://ttc.ninja-web.net/vo-para/index.html (ゆかりPARADISEの後継イベント。)',
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    'Aliases "ゆかりあかりPARADISE" and "ゆかあかパラ": https://x.com/vo_para/status/1112209091353427968',
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    'Alias "yuka-aka-para": transliteration of "ゆかあかパラ" with syntax similar to vo-para',
                    (RT.Guess, OT.Unsourced),
                ),
                Source(
                    "Date: https://web.archive.org/web/20240714193723/http://ttc.ninja-web.net/vo-para/index.html",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Was cancelled alongside vo-para14: https://x.com/vo_para/status/1130104714132111360",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Planned to be simultaneous with VOCALOID PARADISE 14",
            # comments=None,
            last_edited="2026.11.17",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== yukari_paradise ====
    # if i not in disabled_events:
    #     event_name = f"yukari_paradise{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=["ゆかりPARADISE", "Yukari PARADISE ", "ゆかパラ", "yuka-para "],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.11.17",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]
    links = [
        "http://ttc.ninja-web.net/vo-para/",
    ]

    event_group = EventGroup(
        aliases=[
            "ゆかりPARADISE",
            "Yukari PARADISE",
            "ゆかパラ",
            "yuka-para",
            "結月ゆかり・紲星あかりオンリー",
        ],
        events=events,
        media=media,
        links=links,
        sources=[
            Source(
                'Alias "Yukari PARADISE": direct transliteration of "ゆかりPARADISE"',
                (RT.Guess, OT.Unsourced),
            ),
            Source(
                'Alias "ゆかパラ": https://web.archive.org/web/20161104125219/http://ttc.ninja-web.net/vo-para/vo-para11_list.htm',
                (RT.Guess, OT.Unsourced),
            ),
            Source(
                'Alias "yuka-para": from name of the image here: https://web.archive.org/web/20161030214306im_/http://ttc.ninja-web.net/vo-para/yuka-para_s.png',
                (RT.Guess, OT.Unsourced),
            ),
        ],
        comments=None,
        description="Child events of VOCALOID PARADISE event series",
        last_edited="2026.11.17",
    )

    # Check for missing media files and unreferenced media files
    media = [m for e in event_group.events for m in e.media or []] + (
        event_group.media or []
    )
    for m in media:
        if m.path.startswith(("http://", "https://")):
            continue
        p = PATH_MEDIA / m.path
        if not p.exists():
            print(f"Warning: Medium file not found: {p}")

    referenced = {m.path for m in media}
    for p in PATH_MEDIA.rglob("*"):
        if p.is_file() and p.relative_to(PATH_MEDIA).as_posix() not in referenced:
            print(f"Warning: Media file not referenced in event group: {p}")

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
